const quizForm = document.getElementById('quiz-form');
const submitBtn = document.getElementById('submit-btn');
const timerValue = document.getElementById('timer-value');
const timerMessage = document.getElementById('timer-message');
const backBtn = document.getElementById('back-btn');
let timeLeft = 300;

if (quizForm && submitBtn && timerValue) {
    function validateAllQuestions() {
        let isValid = true;
        const questionBlocks = document.querySelectorAll('.question-block');

        questionBlocks.forEach((block) => {
            const chosen = block.querySelector('input[type="radio"]:checked');
            const error = block.querySelector('.error-message');

            if (!chosen) {
                if (error) {
                    error.textContent = 'Please select one answer for this question.';
                }
                isValid = false;
            } else if (error) {
                error.textContent = '';
            }
        });
        return isValid;
    }

    function disableQuiz() {
        submitBtn.disabled = true;
        timerMessage.textContent = 'Time is up. Your answers are being submitted automatically.';
    }

    quizForm.addEventListener('submit', (event) => {
        if (!validateAllQuestions()) {
            event.preventDefault();
            timerMessage.textContent = 'Please answer all questions before submitting.';
        }
    });

    function startTimer() {
        const timerInterval = setInterval(() => {
            timeLeft -= 1;
            timerValue.textContent = timeLeft;

            if (timeLeft <= 0) {
                clearInterval(timerInterval);
                disableQuiz();
                quizForm.submit();
            }
        }, 1000);
    }

    startTimer();
}

if (backBtn) {
    backBtn.addEventListener('click', () => {
        // Show confirmation popup before leaving quiz
        if (confirm("Are you sure you want to go back? Your progress will be lost.")) {
            // Redirect to login/home page
            window.location.href = "/";
        }
    });
}
