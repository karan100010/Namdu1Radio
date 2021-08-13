
 

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
          tracks = playlist.find('a');  
          let comments_playlist={};
          let main_playlist={}
          for(let i=0;i<tracks.length;i++){
          if(tracks.hasOwnProperty(i)){
          if(tracks[i].text.includes("comment")){
          comments_playlist[i]=tracks[i];
          //delete tracks[i]
          }
          else{
          main_playlist[i]=tracks[i]

           }
 
          }}
    main_playlist.length= Object.keys(main_playlist).length

          len = main_playlist.length - 1;
          audio[0].volume = .90;
        //   console.log(playlist.find('a'))
       
          playlist.find('a').click(function(e){
          e.preventDefault();
          link = $(this);
          current = link.parent().index();
          console.log(link);
          run(link, audio[0]);
          
       
         
  });
  $('.collapse').on('show.bs.collapse', function (e) {
    var name=$(e.target).text().replace(/\n/g, '')
    var prefix=name.split("_")[0]
    for(let key in comments_playlist){
      if(comments_playlist.hasOwnProperty(key)){
      if(comments_playlist[key].text.includes(prefix)){
        main_playlist[key]=comments_playlist[key]
        
      }  
      }
      
    }
    main_playlist.length= Object.keys(main_playlist).length
  
  
  })

  $('.collapse').on('show.bs.collapse', function (e) {
    var name=$(e.target).text().replace(/\n/g, '')
    var prefix=name.split("_")[0]
    for(let key in comments_playlist){
      if(comments_playlist.hasOwnProperty(key)){
      if(comments_playlist[key].text.includes(prefix)){
        delete main_playlist[key]
        
      }  
      }
      
    }
    main_playlist.length= Object.keys(main_playlist).length
  
  
  })
  
          audio[0].addEventListener('ended',function(e){
          current++;
          if(current > len){
            // console.log(current)  
            current = 0;
            link = main_playlist[0];
            // console.log(playlist.find('a'))
            // console.log(link)
            
         $.post("./MediaUpload/write_link.php",
         {
           link: link.href,
           
         },
   
         //console.log(x)
         
         )
          }
        else{
          for(let i=0;i< Object.keys(comments_playlist).length+1;i++){
          if(Object.keys(main_playlist).includes(''+current))
          {
            link = main_playlist[current]; 
            console.log("playing")
            run($(link),audio[0]);
            break;
             

          
        }
        else{
          current++
          console.log("skipping")
          console.log(''+current)
          
          
        }}
          
           // console.log(x)
            //let x={"link":link.href};
           
          }
          // 
          });
     }
     function run(link, player){
        player.src = link.attr('href');
        par = link.parent();
        par.addClass('active').siblings().removeClass('active');
        audio[0].load();
        audio[0].play();
        $.post("./MediaUpload/write_link.php",
            {
              link: player.src,
              
            })
     }

    });
  