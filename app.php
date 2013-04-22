<?php
header("Content-Type: text/xml");

class Deterministic {
  public function seed($input) {
    $byte = unpack('S', md5($input, True));
    $two_bits = $byte[1] >> 14;
    $this->decision = $two_bits;
  }

  public function choice($input_array) {
    return $input_array[$this->decision];
  }
}

function answer_for($question) {
  $answers = array('Yes', 'No', 'Maybe', 'Perhaps');
  $determine = new Deterministic();
  $determine->seed($question);
  $answer = $determine->choice($answers);
  return sprintf("<Response><Sms>You asked: '%s', the answer is: '%s'</Sms></Response>\n", $question, $answer);
}

print answer_for($_POST['Body']);
?>
