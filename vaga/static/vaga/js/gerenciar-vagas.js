$(document).ready(function(){
    
    $('#vagasEdicao').DataTable({responsive: true});

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

    var id = $(this).attr('id-vaga');
    var name_form = "form_"+id;
    var form = $('form[name="'+name_form+'"]').serialize();

    $.post('/vaga/editar-vaga/', form, function(data){
        if(data.response === 'ok') {
            $.alert('Sucesso ao salvar os dados da vaga!');
        } else {
            $.alert(data.response)
        }
    });
});

$('.excluir').click(function(e){
    e.preventDefault();
    var _self = $(this);

    $.confirm({
        title: 'Confirmar exclusão:',
        content: 'Deseja mesmo excluir esta vaga?',
        buttons: {
            Confirmar: function () {
                var id = _self.attr('id-vaga');
                $.post('/vaga/excluir-vaga/', {'id': id}, function(data){
                    if(data.response == 'ok') {
                        location.href = "/gerenciar-vagas/";
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

