const assert = require('node:assert/strict');
const { answerFeedback } = require('../assets/quiz.js');
assert.deepEqual(answerFeedback(null, 'b', 'Reason.'), {
  result: 'empty', text: 'Choose an answer first, then check it.'
});
assert.deepEqual(answerFeedback('b', 'b', 'Reason.'), {
  result: 'correct', text: 'Correct. Reason.'
});
assert.deepEqual(answerFeedback('a', 'b', 'Reason.'), {
  result: 'incorrect', text: 'Not quite. Reason.'
});
console.log('PASS: unanswered, correct and incorrect quiz feedback');
