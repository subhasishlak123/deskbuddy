package com.buddy

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.layout.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.Brush
import kotlinx.coroutines.delay

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            var mouthHeight by remember { mutableStateOf(10f) }
            var isBlinking by remember { mutableStateOf(false) }

            // 1. Blinking Logic (Random intervals)
            LaunchedEffect(Unit) {
                while(true) {
                    delay((2000..5000).random().toLong())
                    isBlinking = true
                    delay(100)
                    isBlinking = false
                }
            }

            // 2. The Anime Face UI
            Box(modifier = Modifier.fillMaxSize()) {
                Canvas(modifier = Modifier.fillMaxSize()) {
                    // Realistic Anime Eyes
                    val eyeOpenness = if (isBlinking) 2f else 100f
                    drawOval(
                        color = Color.Black,
                        topLeft = androidx.compose.ui.geometry.Offset(center.x - 150f, center.y - 50f),
                        size = Size(80f, eyeOpenness)
                    )
                    drawOval(
                        color = Color.Black,
                        topLeft = androidx.compose.ui.geometry.Offset(center.x + 70f, center.y - 50f),
                        size = Size(80f, eyeOpenness)
                    )

                    // Lip-Sync Mouth (Moves based on AI voice volume)
                    drawOval(
                        color = Color(0xFFFF6666),
                        topLeft = androidx.compose.ui.geometry.Offset(center.x - 25f, center.y + 150f),
                        size = Size(50f, mouthHeight)
                    )
                }
            }
        }
    }
}
