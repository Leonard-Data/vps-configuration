'use strict';
// Deliberately session-only: quiz answers are not evidence of long-term mastery.
function answerFeedback(selected, correct, explanation) {
  if (selected === null) return { result: 'empty', text: 'Choose an answer first, then check it.' };
  const right = selected === correct;
  return { result: right ? 'correct' : 'incorrect', text: `${right ? 'Correct.' : 'Not quite.'} ${explanation}` };
}
if (typeof document !== 'undefined') {
  document.querySelectorAll('form.quiz').forEach(form => {
    const feedback = form.querySelector('[role="status"]');
    form.addEventListener('submit', event => {
      event.preventDefault();
      const selected = form.querySelector('input:checked');
      const answer = answerFeedback(selected ? selected.value : null, form.dataset.answer, form.dataset.explanation);
      feedback.dataset.result = answer.result;
      feedback.textContent = answer.text;
    });
    form.addEventListener('reset', () => {
      feedback.textContent = '';
      delete feedback.dataset.result;
    });
  });
}
if (typeof module !== 'undefined') module.exports = { answerFeedback };
