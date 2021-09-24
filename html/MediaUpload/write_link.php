<?php

$myfile = fopen("current_link.txt", "w") or die("Unable to open file!");
$txt = $_POST["link"];
fwrite($myfile, $txt);
fclose($myfile);
?> 