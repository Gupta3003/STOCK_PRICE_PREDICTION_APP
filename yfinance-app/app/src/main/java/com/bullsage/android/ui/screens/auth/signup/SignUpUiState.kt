package com.bullsage.android.ui.screens.auth.signup

data class SignUpUiState(
    val email: String = "",
    val password: String = "",
    val passwordVisible: Boolean = false,
    val signUpButtonEnabled: Boolean = true,
    val emailError: String? = null,
    val passwordError: String? = null,
    val errorMessage: String? = null,
    val signUpSuccessful: Boolean = false
)
