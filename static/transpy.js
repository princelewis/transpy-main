$(document).ready(function(){

    $('#dest-state').change(function(){

        let arrival = $('#dest-state option:selected').text()
        let depature = $('#dept-state option:selected').text()

        $('.trans-label').html(`${depature} to ${arrival}`)
        
        $.get("/checkprice?arrival="+arrival, function(data){
            $('#amount p').html(data);
            $('.amountFee').show();   
        })
    })

})
