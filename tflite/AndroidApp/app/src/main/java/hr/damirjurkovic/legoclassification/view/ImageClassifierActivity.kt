package hr.damirjurkovic.legoclassification.view

import android.content.Intent
import android.graphics.Bitmap
import android.net.Uri
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.provider.MediaStore
import hr.damirjurkovic.legoclassification.R
import hr.damirjurkovic.legoclassification.tflite.Classifier
import kotlinx.android.synthetic.main.activity_image_classifier.*

class ImageClassifierActivity : AppCompatActivity() {

    private lateinit var classifier: Classifier
    private val REQUESTIMAGECAPTURE: Int = 101
    private val RESULTLOADIMAGE: Int = 1
    private lateinit var bitmapImage: Bitmap

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_image_classifier)
        setUpUi()
        initClassifier()
    }

    private fun initClassifier() {
        val mInputSize = 224
        val mModelPath = "mobilenetv2_adam_256.tflite"
        val mLabelPath = "label.txt"
        classifier = Classifier(assets, mModelPath, mLabelPath, mInputSize)
    }

    private fun setUpUi() {
        predict.isClickable = false
        capture.setOnClickListener { startCamera() }
        file.setOnClickListener { chooseImage() }
        predict.setOnClickListener { recognizeImage() }
    }

    private fun startCamera() {
        val imageTakeIntent = Intent(MediaStore.ACTION_IMAGE_CAPTURE)

        if (imageTakeIntent.resolveActivity(packageManager) != null) {
            startActivityForResult(imageTakeIntent, REQUESTIMAGECAPTURE)
        }
    }

    private fun chooseImage() {
        val imageIntent = Intent(Intent.ACTION_PICK, MediaStore.Images.Media.EXTERNAL_CONTENT_URI)
        startActivityForResult(imageIntent, RESULTLOADIMAGE)
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        if (requestCode == REQUESTIMAGECAPTURE && resultCode == RESULT_OK) {
            val extras = data?.extras
            bitmapImage = extras?.get("data") as Bitmap
            lego.setImageBitmap(bitmapImage)
            predict.isClickable = true
        }

        if (requestCode == RESULTLOADIMAGE && resultCode == RESULT_OK && null != data) {
            val selectedImage: Uri = data.data!!
            bitmapImage = MediaStore.Images.Media.getBitmap(this.contentResolver, selectedImage)
            lego.setImageBitmap(bitmapImage)
            predict.isClickable = true
        }
    }

    private fun recognizeImage() {
        val result = classifier.recognizeImage(bitmapImage)
        runOnUiThread { updateResults(result) }
    }

    private fun updateResults(result: Pair<String, String>) {
        predictionLabel.text = result.first
        predictionProbability.text = result.second
    }
}