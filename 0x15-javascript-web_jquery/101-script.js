$(document).ready(function () {
$('DIV#add_item').click(function () {
    myList.append('<li>Item</li>');
  });
  $('DIV#remove_item').click(function () {
    myList.find(':last-child').remove();
  });
  $('DIV#clear_list').click(function () {
    myList.empty();
  });
});