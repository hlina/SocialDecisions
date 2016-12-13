//when the Add Field button is clicked
$("#add").click(function (e) {
 //Append a new row of code to the "#items" div
 console.log("hi");
 $("#items").append('<div><input name="input[]" type="text" /><button class="delete">Delete</button></div>'); });


$("body").on("click", ".delete", function (e) {
    $(this).parent("div").remove();
});
