/**
 * create markup for a list of classifications
 */
function changeIt (data) {
	console.log("=============================selected image:" + data);
    //$(dstImg).addClaas('workingImage').siblings('.spinner').remove().after($("<span class='spinner'>&nbsp;</span>"));
	var imageJson = {"Image": data};
    $.ajax({
        type: 'POST',
        url: "http://localhost:8000/select",
		crossDomain: true,
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        data: JSON.stringify(imageJson),
        crossDomain: true,
        error: function (data, textStatus, errorThrown) {
            //console.log(textStatus);
            if (textStatus=="error") {
                textStatus += " failed to send selected image ";
            }
            var errStr = "Error: Failed javascript POST (err: "+textStatus+","+errorThrown+")";
            console.log(errStr);
            return false;
        }
   });
			
}
