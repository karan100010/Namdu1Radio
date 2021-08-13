echo("    
  </button>
</h2>
<label class='custom-file-label' id='$inputlab' for='$fileid'>Choose file</label>
</div>
<div class='input-group-append'>
<button class='btn btn-primary' type='button' id='$inputid' >Upload</button>
</div>
</div>
<div class='progress'>
<div id='progressbar' class='progress-bar bg-success' role='progressbar' style='width: 5%' aria-valuenow='0'
aria-valuemin='0' aria-valuemax='100'></div>
</div> 
<div class='accordion-body'>



<script>
var $fileid = document.getElementById('$fileid');
var $inputlab = document.getElementById('$inputlab');
var submitBtn = document.getElementById('$inputid');
var progressBar = document.getElementById('progressbar');

$fileid.addEventListener('change', function(){handleFileupload($fileid,$inputlab)});
submitBtn.addEventListener('click', function(){uploadFile('$name',$fileid)});
</script>

");