<html>
 <head>
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <style type="text/css">
    #playlist,audio{background:#666;width:400px;padding:20px;}
    .active a{color:#5DB0E6;text-decoration:none;}
    li a{color:#eeeedd;background:#333;padding:5px;display:block;}
    li a:hover{text-decoration:none;}
  </style>
  <script
    type="text/javascript"
    src="./jquery-1.7.js"
    
  ></script>

  <script type="text/javascript">


    $(window).load(function(){
      
    var audio;
    var playlist;
    var tracks;
    var current;

    init();
    function init(){
       	current = 0;
	audio = $('#audio');
    	playlist = $('#playlist');
    	tracks = playlist.find('li a');
    	len = tracks.length - 1;
    	audio[0].volume = .90;
    	playlist.find('a').click(function(e){
          e.preventDefault();
          link = $(this);
          current = link.parent().index();
          run(link, audio[0]);
    	});
    	audio[0].addEventListener('ended',function(e){
          current++;
          if(current > len){
            current = 0;
            link = playlist.find('a')[0];
          }
	  else{
            link = playlist.find('a')[current];    
          }
          run($(link),audio[0]);
    	});
     }
     function run(link, player){
        player.src = link.attr('href');
        par = link.parent();
        par.addClass('active').siblings().removeClass('active');
        audio[0].load();
        audio[0].play();
     }

    });

  </script>
 </head>
 <body>
  <div id="topMenu" style="display:flex; flex-direction: row;">
	<a href="/MediaUpload/gallery.php" style="padding: 10px; background-color: #000000; color: #ffffff">Visual Gallery</a>
	<a href="/MediaUpload/upload.html" style="padding: 10px; background-color: #000000; color: #ffffff">Upload Image/Video</a>
  </div>
  <center>
   <div > <img src="wallpaper.jpg" style="width:100%;height:70%"> </div>
   <br>	
   <font size="10px">  Programs </font> 

   <br><br>	
 <?php
    
     // Opens directory
     $myDirectory=opendir("/var/www/html/.upload/cat5/");

     // Gets each entry
     while($entryName=readdir($myDirectory)) {
      $dirArray[]=$entryName;
     }

     // Finds extensions of files
     function findexts($filename) {
      for ($i=0;$filename[$i]!=NULL;$i++){}
	$exts = $filename[$i-1];
      return $exts;
     }

     // Closes directory
     closedir($myDirectory);

     // Counts elements in array
     $indexCount=count($dirArray);

     // Sorts files
     //sort($dirArray);
       rsort($dirArray);//sorting in descending order
	
     $flag=0;
     
     
     // (Randomly) Loops through the array of files
     for($index=rand(0,$indexCount); $index < $indexCount; $index++) {
      
      //Loops through the array of files
      //for($index=0; $index < $indexCount; $index++) {
      
      // Gets File Names
      $name=$dirArray[$index];
      $namehref=$dirArray[$index];	
      $ext = findexts($name);
	
      if ($ext=='3'){
	
	if ($flag==0){
	 // Print 'em
  	 print("
	  <audio autoplay id='audio' preload='auto' tabindex= '0' controls='' type='audio/mpeg'>
           <source src='./.upload/cat5/$namehref'>
           Sorry, your browser does not support HTML5 audio.
          </audio>
		

	  <ul id='playlist'>
     	 ");
      	 print("
      	  
           <li class='active'>
 	    <a href='./.upload/cat5/$namehref'>$name</a>
 	   </li>
	        <button>Click</button>
	     ");
	 $flag=1;
	}
	else{      
         // Print 'em
         print("
          
           <li>
	     <a href='./.upload/cat5/$namehref'>$name</a>
	   </li>
	 ");
        }
       }
      }
      
    ?>
	
   </ul> 	
  </center>
 </body>
</html>
