$(document).ready(function(){
    $(".relatorioTabela").DataTable( );

    var csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
});


$('.salvar').click(function(e){
    e.preventDefault();
    var id = $(this).attr('id-candidatura');
    var name_form = "form_"+id;
    var form = $('form[name="'+name_form+'"]').serialize();

    $.post('/vaga/editar-candidatura/', form, function(data){
        if(data.response === 'ok') {
            $.alert('Sucesso ao salvar os dados da candidatura!');
        } else {
            $.alert(data.response)
        }
    });
});

$('.excluir').click(function(e){
    e.preventDefault();
    var _self = $(this);
    var id_vaga = $(this).attr('id-vaga');
    var total_validas = parseInt($("#total_validas_"+id_vaga).html());

    $.confirm({
        title: 'Confirmar exclusão:',
        content: 'Deseja mesmo excluir esta candidatura?',
        buttons: {
            Confirmar: function () {
                var table = $(".relatorioTabela").DataTable( );
                var id = _self.attr('id-candidatura');
                var tr = _self.closest('tr');
                $.post('/vaga/excluir-candidatura/', {'id': id}, function(data){
                    if(data.response == 'ok') {
                        $.alert('Sucesso ao remover candidatura.');
                        if (total_validas > 0) {
                            total_validas = total_validas - 1;
                            $("#total_validas_"+id_vaga).html(total_validas)
                        }
                        table.row(tr).remove().draw();
                    } else {
                        $.alert(data.response);
                    }
                });
            },
            Cancelar: function () {
            }
        }
    });
});
