window.Superlists = {};
window.Superlists.initialize = function () {
	console.log("Initialized")
	$('input[name="text"]').on('keypress', function () {
		$('.has-error').hide();
	});
};