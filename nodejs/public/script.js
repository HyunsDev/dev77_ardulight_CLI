function command_send() {
    var port = $("#port").val();
    var command = $("#command").val();


    if (port == "") {
        $("#send").addClass("warn")
            $("#send").val("Fill Port")
            setTimeout(function() {
                $("#send").removeClass("warn")
                $("#send").val("Send")
            }, 500);
    } else {
        $("#command").val("");
        $.ajax({
            url: "/a/" + port,
            data: {d: command},
            type: "GET",
            dataType: "json"
        }).done(function(json) {
            if (json.result == "ok") {
                $("#send").addClass("ok")
                $("#send").val("Good!")
                setTimeout(function() {
                    $("#send").removeClass("ok")
                    $("#send").val("Send")
                }, 500);

            } else {
                $("#send").addClass("warn")
                $("#send").val("ERROR")
                setTimeout(function() {
                    $("#send").removeClass("warn")
                    $("#send").val("Send")
                }, 500);
            }
        })
    }
}

function fill(name) {
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
            $("#command").val("each([[255, 0, 0], [255, 98, 0], [255, 153, 0], [255, 213, 0], [242, 255, 0], [162, 255, 0], [85, 255, 0], [0, 255, 119], [0, 255, 183], [0, 242, 255], [0, 174, 255], [0, 98, 255], [128, 0, 255], [195, 0, 255], [255, 0, 251], [255, 0, 166], [255, 255, 255], [0, 0, 0]])");
            break

        case "spac":
            $("#command").val("spac(30)");
            break

        case "wave":
            $("#command").val("wave(30, [[255, 0, 0], [255, 98, 0], [255, 153, 0], [255, 213, 0], [242, 255, 0], [162, 255, 0], [85, 255, 0], [0, 255, 119], [0, 255, 183], [0, 242, 255], [0, 174, 255], [0, 98, 255], [128, 0, 255], [195, 0, 255], [255, 0, 251], [255, 0, 166], [255, 255, 255], [0, 0, 0]])");
            break

        case "down":
            $("#command").val("down(30, [255,255,0])");
            break

        case "wipe":
            $("#command").val("wipe(30, [[255, 0, 0], [255, 98, 0], [255, 153, 0], [255, 213, 0], [242, 255, 0], [162, 255, 0], [85, 255, 0], [0, 255, 119], [0, 255, 183], [0, 242, 255], [0, 174, 255], [0, 98, 255], [128, 0, 255], [195, 0, 255], [255, 0, 251], [255, 0, 166], [255, 255, 255], [0, 0, 0]])");
            break

        case "raw":
            $("#command").val(`raw("")`);
            break
            
        
    }


}