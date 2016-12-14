$(document).ready(function() {
	var date_input=$('input[name="date"]'); //our date input has the name "date"
	var container=$('.bootstrap-iso form').length>0 ? $('.bootstrap-iso form').parent() : "body";
	var options={
	    format: 'mm/dd/yyyy',
	    container: container,
	    todayHighlight: true,
	    autoclose: true,
	};
	date_input.datepicker(options);
   //when the Add Field button is clicked
    $("#add").click(function (event) {
     //Append a new row of code to the "#items" div
     $("#items").append('<div><input class="form-control" name="option" type="text" placeholder = "Option"/><a href = "#" class="delete">Delete</a><br><br></div>'); });


    $("body").on("click", ".delete", function (event) {
        $(this).parent("div").remove();
    });

}());
