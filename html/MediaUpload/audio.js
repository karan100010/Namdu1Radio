
 

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
            console.log(audio)
            
            
            console.log(tracks[0]["href"]) 
            $.post("MediaUpload/write_link.php",
              {
                link: tracks[0]["href"],
                
              },function(d,s){console.log(s)}
        
              //console.log(x)
              
              )
            } 
            
            
            
            
            len = tracks.length - 1;
            audio[0].volume = .90;
            playlist.find('a').click(function(e){
            e.preventDefault();
            link = $(this);
        
            current = link.parent().index();
            link
        
            run(link, audio[0]);
            
            });
            
            audio[0].addEventListener('ended',function(e){
            current++;
            if(current > len){
              current = 0;
              link = playlist.find('a')[0];
              
           //   console.log(link.href)
              
           
            }
          else{
              link = playlist.find('a')[current]; 
             // console.log(x)
              //let x={"link":link.href};
              
            }
            if(typeof link!=='undefined'){
            run($(link),audio[0]);
            $.post("MediaUpload/write_link.php",
              {
                link: link.href,
                
              },function(d,s){console.log(s)}
        
              //console.log(x)
              
              )
            }
          else{
            current++
          }});
       
       function run(link, player){
          player.src = link.attr('href');
          par = link.parent();
          par.addClass('active').siblings().removeClass('active');
          audio[0].load();
          audio[0].play();
          $.post("MediaUpload/write_link.php",
              {
                link: player.src,
                
              })
       }
  
      });
  
