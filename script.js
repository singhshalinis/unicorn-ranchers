document.getElementById('forest').addEventListener('click', function() {
    alert("forest:before");

    var unicornName = document.getElementById('unm').textContent;
    var newurl = "changestate/" + unicornName  + "/" + "Forest";

    $.ajax({
        url: newurl,
        type: "POST",
        success: function(data) {
            alert("forest:after");
            console.log("Done!");
        }
    });
});

/* Same for other buttons */
