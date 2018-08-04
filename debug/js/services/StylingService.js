BH.add('StylingService', function() {
	
	"use strict";
    eval(BH.System);

    var StylingService = BH.Class(BH.Widget, {

		// Stub
        save_user_info: function(data, successCb, errorCb) {
		
			var random = Math.floor(Math.random() * (2));

			var date = new Date(1543000626 * 1000);
			var formattedDate = (date.getMonth() + 1) + '/' + date.getDate() + '/' + date.getFullYear();
			var formattedTime = date.getHours() + ':' + date.getMinutes() + ' ' + (date.getHours() >= 12 ? 'pm' : 'am');
			var timezone = date.toLocaleTimeString('en-us',{ timeZoneName:'short' }).split(' ')[2];
			var formattedDateTime = formattedDate + ' ' + formattedTime + ' ' + timezone;
			
			if (random === 0) {
				if (successCb) {
					successCb({
						'scheduled_appointment_date': formattedDateTime,
						'first_name': data.first_name
					});
				}
			} else {
				if (errorCb) {
					errorCb('Sorry, something went wrong.');
				}
			}			
        }

    });

    if (!BH.StylingService) {
        BH.StylingService = new StylingService();
        BH.StylingService.render();
    }
});
