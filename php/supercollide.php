<?php
/*
  Inserting 65536 evil elements took 93.333761930466 seconds
  Inserting 65536 good elements took 0.027647018432617 seconds
*/
//echo '<pre>';

$size = pow(2, 16); // 16 is just an example, could also be 15 or 17

$startTime = microtime(true);

$array = array();
for ($key = 0, $maxKey = ($size - 1) * $size; $key <= $maxKey; $key += $size) {
    $array[$key] = 0;
}

$endTime = microtime(true);

echo 'Inserting ', $size, ' evil elements took ', $endTime - $startTime, ' seconds', "\n";

$startTime = microtime(true);

$array = array();
for ($key = 0, $maxKey = $size - 1; $key <= $maxKey; ++$key) {
    $array[$key] = 0;
}

$endTime = microtime(true);

echo 'Inserting ', $size, ' good elements took ', $endTime - $startTime, ' seconds', "\n";
