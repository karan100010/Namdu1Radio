<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <title>Gallery</title>
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="assets/css/bootstrap.min.css">
    <link type="text/css" rel="stylesheet" href="lightgallery.js/dist/css/lightgallery.css" /> 
    <link rel="stylesheet" href="assets/css/gallery.css">
    <style>
    #lightgallery{
    
    }
    #lightgallery > a > img{
        max-width: 250px;
        padding: 5px;
        border: 3px solid;
        border-color: #ffffff;
        }
	#btn-home{
		position: fixed;
		left: 10px;	
	}
	#btn-upload{
		position: fixed;
		right: 10px;
	}
    </style>
</head>

<body class="home">
   <div id="menu" style="display: flex; flex-direction: row;  width: 100%; align-items: center; position:fixed; top:0; justify-content: center;">
	<div>
		<a href="/" id="btn-home"><button type="button" class="btn btn-warning">🏠Home</button></a>
		<a href="upload.html" id="btn-upload"><button type="button"  class="btn btn-warning">⬆️Upload</button></a>
	</div>
   </div>
   <div id="lightgallery" style="display:flex; flex-direction: column; justify-content: center; align-items: center; margin-top: 35px;">
           <?php require('scan_files.php'); ?>
    </div>
    <script src="assets/js/picturefill.min.js"></script>
    <script src="assets/js/lightgallery/lightgallery.js"></script>
    <script src="assets/js/lightgallery/lg-pager.js"></script>
    <script src="assets/js/lightgallery/lg-autoplay.js"></script>
    <script src="assets/js/lightgallery/lg-fullscreen.js"></script>
    <script src="assets/js/lightgallery/lg-zoom.js"></script>
    <script src="assets/js/lightgallery/lg-hash.js"></script>
    <script src="assets/js/lightgallery/lg-share.js"></script>
    <script>
        lightGallery(document.getElementById('lightgallery'));
    </script>
</body>

</html>
