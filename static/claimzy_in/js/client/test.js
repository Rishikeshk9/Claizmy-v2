const controller = new ScrollMagic.Controller();
const tlFirstScroll = new TimelineMax();
const tlSecondScroll = new TimelineMax();

//First scroll scene
tlFirstScroll
.set('.iphone-image-wrapper', {scale: 4, transformOrigin: 'center top'})
.to('.iphone-image-wrapper', 3, {
    scale: 2.2,
    y: '-50%'
})
.to('.iphone-image-wrapper', 3, {
    scale: 1,
    y: '0%'
})

//Second scroll scene
tlSecondScroll
.to('.iphone1', 3, {x: '-50%'})
.to('.iphone2', 3, {x: '50%'}, '-=3')
.from('.iphone1-text', 0.3, {autoAlpha: 0}, '-=3')
.from('.iphone2-text', 0.3, {autoAlpha: 0}, '-=3')
.to('.iphone1-text', 3, {x: '-30%'}, '-=3')
.to('.iphone2-text', 3, {x: '30%'}, '-=3')

.set('.iphone-stick', {display: 'block'})
.to('.iphone1-img-behind', 3, {x: '-50%'})
.to('.iphone2-img-behind', 3, {x: '60%'}, '-=3')
.to('.iphone1-img', 0.3, {autoAlpha: 0}, '-=3')
.to('.iphone2-img', 0.3, {autoAlpha: 0}, '-=3')
.to('.iphone1-text', 1, {autoAlpha: 0}, '-=3')
.to('.iphone2-text', 1, {autoAlpha: 0}, '-=3')



//Scene 1
const sceneOne = new ScrollMagic.Scene({
    triggerElement: '.trigger1',
    triggerHook: 0,
    duration: '100%'
})
.setTween(tlFirstScroll)
.addTo(controller)


const sceneTwo = new ScrollMagic.Scene({
    triggerElement: '.trigger2',
    triggerHook: 0,
    duration: '100%'
})
.setTween(tlSecondScroll)
.setPin('.trigger2')
.addTo(controller)