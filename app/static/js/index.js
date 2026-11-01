// https://dev.to/webdiscus/3d-parallax-effect-by-moving-mouse-using-htmlcss-7b2

document.addEventListener("mousemove", (event) => {
    const root = document.documentElement;

    const smoothMove = 0.05;
    const rotateX = (event.clientY - window.innerHeight / 2) * smoothMove;
    const rotateY = ((event.clientX - window.innerWidth / 2) * -smoothMove) / 2;

    root.style.setProperty("--paralax-x", `${rotateX}deg`);
    root.style.setProperty("--paralax-y", `${rotateY}deg`);
});

let mouseX = 0;
let mouseY = 0;
let flashlight;

const isTouchDevice = () => {
    try {
        document.createEvent("TouchEvent");
        return true;
    } catch (e) {
        return false;
    }
};

function getMousePosition(e) {
    mouseX = !isTouchDevice() ? e.pageX : e.touches[0].pageX;
    mouseY = !isTouchDevice() ? e.pageY : e.touches[0].pageY;

    flashlight.style.setProperty("--flashlight-x", mouseX + "px");
    flashlight.style.setProperty("--flashlight-y", mouseY + "px");
}

document.addEventListener("DOMContentLoaded", () => {
    flashlight = document.getElementById("flashlight");

    document.addEventListener("mousemove", getMousePosition);
    document.addEventListener("touchmove", getMousePosition);
});
