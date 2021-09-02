<?php
$dir    = 'ready_to_display/';
$files = array_diff(scandir($dir,1), array('..', '.'));

foreach($files as $file){
   echo '
<a class="gallery-img-link" href="ready_to_display/'.$file.'">
      <img class="gallery-img" src="ready_to_display/'.$file.'"/>
  </a>
  ';
}

?>
 
