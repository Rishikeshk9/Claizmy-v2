var scene = document.getElementById('scene');
var parallaxInstance = new Parallax(scene);
window.onload = function(){
     $("#navbar1").height(45); 
};
 

window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
     
    $("#navbar1").height(45);
    $("#navbar-img").height(30)

  } else { 
    $("#navbar1").height(60);
    $("#navbar-img").height(45)
  }
}
ScrollReveal().reveal('.card1',{ delay: 200 });
ScrollReveal().reveal('.card2', { delay: 500 }); 

ScrollReveal().reveal('.card3',{ delay: 800 });
ScrollReveal().reveal('.card4', { delay: 200 }); 

ScrollReveal().reveal('.card5',{ delay: 500 });
ScrollReveal().reveal('.card6', { delay: 800 }); 

function getOffset(el) {
    const rect = el.getBoundingClientRect();
    return {
      left: rect.left + window.scrollX,
      top: rect.top + window.scrollY
    };
  }

// init controller
var controller = new ScrollMagic.Controller();
$(function () { // wait for document ready
    //liquid
    var loc = "https://assets10.lottiefiles.com/packages/lf20_dBbqyA.json";
    
// build scene
var scen = new ScrollMagic.Scene({triggerElement: "#trigger1",  triggerHook: 0,  })
								 
                .on("start", function(e) { 
                if (e.scrollDirection === "FORWARD") {
                  $("#pin1").stick_in_parent()
                  .on("sticky_kit:stick", function(e) {
                    console.log("has stuck!", e.target);
                  })
                  .on("sticky_kit:unstick", function(e) {
                    console.log("has unstuck!", e.target);
                  });
                   
                    }
                    if (e.scrollDirection === "REVERSE") {
                   
                   $('#wall').css('background-color', '#fff');
                   }
                }) 
								.addTo(controller);
                var scene = new ScrollMagic.Scene({triggerElement: "#trigger1",  triggerHook: "onLeave"  })     
                .on("start", function(e) { 
                    var $tText = $('#name');
                    if (e.scrollDirection === "FORWARD") {
                      $('#name').css('opacity', '1');
                        $tText.html(
                            '<div id="anim" class=" " style="width: 150px;height: 150px;"> </div> <br><br>Liquid/Water <br>  Damage'); 
                            $('#wall').css('background-color', '#fff');
                            lottie.loadAnimation({
                                container: document.getElementById('anim'), // the dom element that will contain the animation
                                renderer: 'svg',
                                loop: true,
                                autoplay: true,
                                path: loc // the path to the animation json
                              });
                        }
                        if (e.scrollDirection === "REVERSE") {
                          $('#name').css('opacity', '0');
                       $('#wall').css('background-color', '#fff');
                       }
                    })
                                    
                                 
								.addTo(controller);


                var scene2 = new ScrollMagic.Scene({triggerElement: "#trigger2"      })               
                .on("start", function(e) { 
                    var $tText = $('#name');
                    if (e.scrollDirection === "FORWARD") {
                        var loc = "https://assets1.lottiefiles.com/datafiles/pszsjowZZRqCzTz/data.json";

                        $tText.html(
                            '<div id="anim" class=" " style="width: 150px;height: 150px;"> </div>  <br>Cracked/Broken<br> Screen'); 
                           
                            $('#wall').css('background-color', '#0399e0');
                            $tText.css("color","white") 

                            lottie.loadAnimation({
                                container: document.getElementById('anim'), // the dom element that will contain the animation
                                renderer: 'svg',
                                loop: true,
                                autoplay: true,
                                path: loc // the path to the animation json
                              });
                        }

                        if (e.scrollDirection === "REVERSE") {
                             //liquid
                            var loc = "https://assets10.lottiefiles.com/packages/lf20_dBbqyA.json";
                            
                            $tText.html(
                                '<div id="anim" class=" " style="width: 150px;height: 150px;"> </div> <br><br>Liquid/Water <br>  Damage'); 
                                $('#wall').css('background-color', '#fff'); 
                                $tText.css("color","black")
                            lottie.loadAnimation({
                                container: document.getElementById('anim'), // the dom element that will contain the animation
                                renderer: 'svg',
                                loop: true,
                                autoplay: true,
                                path: loc // the path to the animation json
                              });
                       }

                       
                    })
                                           
								.addTo(controller);

                
                var scene3 = new ScrollMagic.Scene({triggerElement: "#trigger3"     })                
                .on("start", function(e) { 
                    var $tText = $('#name');
                    if (e.scrollDirection === "FORWARD") {
                        //unresponsive
                       var loc = "https://assets1.lottiefiles.com/packages/lf20_w7jpC5.json";
                        $tText.html(
                            '<div id="anim" class=" m-auto " style="width: 150px;height: 150px;"> </div> <br><br>Unresponsive/Dead<br>  Touchpad'); 
                            $('#wall').css('background-color', '#f44336'); 
                            $tText.css("color","black") 
                               
                            lottie.loadAnimation({
                                container: document.getElementById('anim'), // the dom element that will contain the animation
                                renderer: 'svg',
                                loop: true,
                                autoplay: true,
                                path: loc // the path to the animation json
                              });
                        }
                        if (e.scrollDirection === "REVERSE") {
                            //crackedscreen
                            var loc = "https://assets1.lottiefiles.com/datafiles/pszsjowZZRqCzTz/data.json";

                            $tText.html(
                                '<div id="anim" class=" " style="width: 150px;height: 150px;"> </div>  <br>Cracked/Broken<br>  Screen'); 
                               
                                $('#wall').css('background-color', '#0399e0');
                                $tText.css("color","white") 
    
                                lottie.loadAnimation({
                                    container: document.getElementById('anim'), // the dom element that will contain the animation
                                    renderer: 'svg',
                                    loop: true,
                                    autoplay: true,
                                    path: loc // the path to the animation json
                                  }); 
                       }
                    })
                                        
								.addTo(controller);           

                
                
                var scene5 = new ScrollMagic.Scene({triggerElement: "#trigger4"   })                 
                .on("start", function(e) { 
                    var $tText = $('#name');
                    if (e.scrollDirection === "FORWARD") {
                      //broken charging
                       var loc = "https://assets10.lottiefiles.com/datafiles/nXSZkMBrKvjQPD1YghNc44DYDd78Num4T6cOpHtU/AE_JSON/47-Battery.json";
                        $tText.html(
                            '<div id="anim" class=" m-auto centered" style="width: 200px;height: 200px;"> </div><br><br><br><br><br><br> Broken Charging<br> Port'); 
                            $('#wall').css('background-color', '#ffbc01');
                            $tText.css("color","black") 
                          lottie.loadAnimation({
                            container: document.getElementById('anim'), // the dom element that will contain the animation
                            renderer: 'svg',
                            loop: true,
                            autoplay: true,
                            path: loc // the path to the animation json
                          });
                        }
                        if (e.scrollDirection === "REVERSE") {
                          //unresponsive
                       var loc = "https://assets1.lottiefiles.com/packages/lf20_w7jpC5.json";
                        $tText.html(
                            '<div id="anim" class=" m-auto " style="width: 150px;height: 150px;"> </div> <br><br>Unresponsive/Dead<br>  Touchpad'); 
                            $('#wall').css('background-color', '#ffc400'); 
                            $tText.css("color","black") 
                               
                            lottie.loadAnimation({
                                container: document.getElementById('anim'), // the dom element that will contain the animation
                                renderer: 'svg',
                                loop: true,
                                autoplay: true,
                                path: loc // the path to the animation json
                              });
                       }
                    })
                                    
								.addTo(controller);      



                var scene4 = new ScrollMagic.Scene({triggerElement: "#trigger5"   })                 
                .on("start", function(e) { 
                    var $tText = $('#name');
                    if (e.scrollDirection === "FORWARD") {
                       //faulty Earphones
                       var loc = "https://assets5.lottiefiles.com/packages/lf20_ML9uCF.json";
                        $tText.html(
                            '<div id="anim" class=" m-auto " style="width: 150px;height: 150px;"> </div>  Faulty Earphone<br> Jack'); 
                            $('#wall').css('background-color', '#4caf50'); //#4527a0
                            $tText.css("color","white") 

                            
                           lottie.loadAnimation({
                            container: document.getElementById('anim'), // the dom element that will contain the animation
                            renderer: 'svg',
                            loop: true,
                            autoplay: true,
                            path: loc // the path to the animation json
                          });
                        }
                        if (e.scrollDirection === "REVERSE") {
                            //broken charging
                       var loc = "https://assets10.lottiefiles.com/datafiles/nXSZkMBrKvjQPD1YghNc44DYDd78Num4T6cOpHtU/AE_JSON/47-Battery.json";
                       $tText.html(
                           '<div id="anim" class=" m-auto centered" style="width: 200px;height: 200px;"> </div><br><br><br><br><br><br> Broken Charging<br> Port'); 
                           $('#wall').css('background-color', '#ffbc01');
                           $tText.css("color","black") 
                         lottie.loadAnimation({
                           container: document.getElementById('anim'), // the dom element that will contain the animation
                           renderer: 'svg',
                           loop: true,
                           autoplay: true,
                           path: loc // the path to the animation json
                         });
                       }
                    })
                                         
								.addTo(controller);      


                var scene6 = new ScrollMagic.Scene({triggerElement: "#trigger6"     })                 
                .on("start", function(e) { 
                  var $tText = $('#name');
                if (e.scrollDirection === "FORWARD") {
                  $('#wall').css('background-color', '#fff');                 
                  $("#sticky_item").trigger("sticky_kit:unstick");
                //faulty Earphones
                var loc = "https://assets5.lottiefiles.com/packages/lf20_ML9uCF.json";
                $tText.html(
                    '<img src="/static/claimzy_in/img/logo-dark.png" alt="claim"  width="200px" class=" m-auto p-1 " alt="Claim Now">'); 
                     
                    $tText.css("color","black")
                    }
                    if (e.scrollDirection === "REVERSE") {

                      $('#name').css('opacity', '100%');
                    //faulty Earphones
                    var loc = "https://assets5.lottiefiles.com/packages/lf20_ML9uCF.json";
                    $tText.html(
                        '<div id="anim" class=" m-auto " style="width: 150px;height: 150px;"> </div>  Faulty Earphone<br> Jack'); 
                        $('#wall').css('background-color', '#4caf50'); //#4527a0
                        $tText.css("color","white") 

                        
                      lottie.loadAnimation({
                        container: document.getElementById('anim'), // the dom element that will contain the animation
                        renderer: 'svg',
                        loop: true,
                        autoplay: true,
                        path: loc // the path to the animation json
                      });
                   }    
                })
                
                .addTo(controller); 



                var scene6 = new ScrollMagic.Scene({triggerElement: "#trigger7", triggerHook: '1'    })                 
                .on("start", function(e) { 
                  var $tText = $('.navbar-brand');
                if (e.scrollDirection === "FORWARD") {
                  //$tText.css('opacity', '0');                 
                   
                    }
                    if (e.scrollDirection === "REVERSE") {

                      $tText.css('opacity', '1');
                   }    
                }) 
                
                .addTo(controller); 


 
  }); 
  $('.slides').slick({
    dots: true,
    infinite: true, 
    slidesToShow: 7,
    focusOnSelect: false,
  slidesToScroll: 1,
  autoplay: true,
  autoplaySpeed: 2000,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 3,
          infinite: true,
          dots: true
        }
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 2
        }
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 3,
          slidesToScroll:2
        }
      }
      // You can unslick at a given breakpoint now by adding:
      // settings: "unslick"
      // instead of a settings object
    ]
  });


  $("#about").click(function() {
    $('html,body').animate({
        scrollTop: $(".about-section").offset().top},
        'slow');
});

$("#contact").click(function() {
  $('html,body').animate({
      scrollTop: $(".contact-section").offset().top},
      'slow');
});
var loc = "static/claimzy_in/anim/gadgets.json";
      lottie.loadAnimation({
                        container: document.getElementById('about-anim'), // the dom element that will contain the animation
                        renderer: 'svg',
                        loop: true,
                        autoplay: true,
                        path: loc // the path to the animation json
      });

 
        var loc = "https://assets1.lottiefiles.com/packages/lf20_lD3kss.json";
    lottie.loadAnimation({
        container: document.getElementById('anim2'), // the dom element that will contain the animation
        renderer: 'svg',
        loop: true,
        autoplay: true,
        path: loc // the path to the animation json
      });

      var loc = "https://assets10.lottiefiles.com/packages/lf20_3bWFWj.json";
      lottie.loadAnimation({
          container: document.getElementById('anim3'), // the dom element that will contain the animation
          renderer: 'svg',
          loop: true,
          autoplay: true,
          path: loc // the path to the animation json
        });
        

        
      var loc = "https://assets4.lottiefiles.com/packages/lf20_EEU4nQ.json";
      lottie.loadAnimation({
          container: document.getElementById('anim4'), // the dom element that will contain the animation
          renderer: 'svg',
          loop: true,
          autoplay: true,
          path: loc // the path to the animation json
        });


        

        var loc = "https://assets5.lottiefiles.com/packages/lf20_yZpLO2.json";
      lottie.loadAnimation({
          container: document.getElementById('anim5'), // the dom element that will contain the animation
          renderer: 'svg',
          loop: true,
          autoplay: true,
          path: loc // the path to the animation json
        });

        var loc = "https://assets1.lottiefiles.com/packages/lf20_KMustJ.json";
      lottie.loadAnimation({
          container: document.getElementById('anim6'), // the dom element that will contain the animation
          renderer: 'svg',
          loop: true,
          autoplay: true,
          path: loc // the path to the animation json
        });

        

        var loc = "https://assets7.lottiefiles.com/temp/lf20_YsothS.json";
        lottie.loadAnimation({
            container: document.getElementById('anim7'), // the dom element that will contain the animation
            renderer: 'svg',
            loop: true,
            autoplay: true,
            path: loc // the path to the animation json
          });


          var modal = document.querySelector(".modal");
          var trigger = document.querySelector(".trigger");
          var closeButton = document.querySelector(".close-modal");
      
          function toggleModal() {
              modal.classList.toggle("show-modal");
          }
      
          function windowOnClick(event) {
              if (event.target === modal) {
                  toggleModal();
              }
          }
      

          trigger.addEventListener("click", toggleModal);
         closeButton.addEventListener("click", toggleModal);
          window.addEventListener("click", windowOnClick);