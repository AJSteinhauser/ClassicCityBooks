     $(function () {
        $("#keepcardinfo").click(function () {
            if ($(this).is(":checked")) {
                $("#newcard").removeAttr("disabled");
				$("#expdate").removeAttr("disabled");
                $("#ccv").removeAttr("disabled");
				$("#cardzipc").removeAttr("disabled");				
            } else {
                $("#newcard").attr("disabled", "disabled");
				$("#expdate").attr("disabled", "disabled");
                $("#ccv").attr("disabled", "disabled");
				$("#cardzipc").attr("disabled", "disabled");				
            }
        });
    });
	
	  $(function () {
        $("#changepassword").click(function () {
            if ($(this).is(":checked")) {
                $("#currpass").removeAttr("disabled");
				$("#newpass").removeAttr("disabled");
                $("#confirmpass").removeAttr("disabled");			
            } else {
                $("#currpass").attr("disabled", "disabled");
				$("#newpass").attr("disabled", "disabled");
                $("#confirmpass").attr("disabled", "disabled");				
            }
        });
    });
