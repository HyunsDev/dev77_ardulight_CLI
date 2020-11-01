
// import { ipcRenderer } from 'electron';

var ipcRenderer = require("electron")

function command_send() {
    var port = $("#port").val();
    var command = $("#command").val();

    var data = {
        port: port,
        command: command
    }
    
    
    if (port == "") {
        $("#send").addClass("warn")
            $("#send").val("Fill Port")
            setTimeout(function() {
                $("#send").removeClass("warn")
                $("#send").val("Send")
            }, 500);
    } else {
        $("#command").val("");
        $("#send").val("Sending..")
        $("#send").addClass("sending")

        ipcRenderer.ipcRenderer.send("ardulight_1", data)

        ipcRenderer.ipcRenderer.on("ardulight_2", (event, contents) => {
            console.log(contents.result)

            if(contents.result == "err") {
                console.log(contents.error)
            }

            if (contents.result == "ok") {
                $("#send").removeClass("sending")
                $("#send").addClass("ok")
                $("#send").val("Good!")
                setTimeout(function() {
                    $("#send").removeClass("ok")
                    $("#send").val("Send")
                }, 1000);
            } else if (contents.result == "err") {
                $("#send").removeClass("sending")
                $("#send").addClass("warn")
                $("#send").val("ERROR")
                setTimeout(function() {
                    $("#send").removeClass("warn")
                    $("#send").val("Send")
                }, 1000);
                console.log(contents.error)
            }
        })
    }
    }
    
    function fill(name) {
    let teat_array = "[[255, 0, 0], [255, 77, 0], [255, 153, 0], [255, 229, 0], [204, 255, 0], [128, 255, 0], [51, 255, 0], [0, 255, 25], [0, 255, 102], [0, 255, 179], [0, 255, 255], [0, 178, 255], [0, 102, 255], [0, 25, 255], [51, 0, 255], [128, 0, 255], [204, 0, 255], [255, 0, 230]]"
    
    switch (name) {
        case "on":
            $("#command").val("on()");
            break
    
        case "off":
            $("#command").val("off()");
            break
    
        case "soild":
            $("#command").val("soild([255,255,255])");
            break
    
        case "each":
            $("#command").val(`each(${teat_array})`);
            break
    
        case "spac":
            $("#command").val("spac(30)");
            break
    
        case "wave":
            $("#command").val(`wave(30, ${teat_array})`);
            break
    
        case "down":
            $("#command").val("down(30, [255,255,0])");
            break
    
        case "wipe":
            $("#command").val(`wipe(30, ${teat_array})`);
            break
    
        case "raw":
            $("#command").val(`raw("")`);
            break
    }
    }

setTimeout(function() {
    $(".loading").css("display", "none")
}, 3000)