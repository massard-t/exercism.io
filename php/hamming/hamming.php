<?php

//
// This is only a SKELETON file for the "Hamming" exercise. It's been provided as a
// convenience to get you started writing code faster.
//

function distance($a, $b)
{
	if (strlen($a) != strlen($b)) {
		throw new InvalidArgumentException('DNA strands must be of equal length.');
	}
	$len = strlen($a);
	$count = 0;
	for ($i = 0; $i < $len; $i++) {
		if ($a[$i] != $b[$i]) {
			$count++;
		}
	}
	return $count;
}
