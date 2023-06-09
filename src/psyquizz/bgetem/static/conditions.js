$(document).ready(function() {
    var button = $('input[type=submit][name="form.action.add"]');
    var conditions = $('input[type=radio][name="form.field.accept"]');

    let e = $("<p></p>");
    $("#field-form-field-accept").append(e)
    e.hide()
    e.html("<p> Die Nutzung des Online Tools ist ausschließlich bei der BG ETEM versicherten Betrieben vorbehalten.  </p>");

    let f = $("<p></p>");
    $("#field-form-field-accept").append(f)
    f.hide()
    //f.html("<p>Hiermit bestätige ich, dass ich die Online Plattform für einen bei der BG ETEM versicherten Betrieb nutze.</p>");

    if ($('input:radio[name="form.field.accept"][value=ja]').is(':checked')) {
        button.prop('disabled', false);
        e.hide();
        f.show();
    } else {
        button.prop('disabled', true);
        if ($('input:radio[name="form.field.accept"][value=nein]').is(':checked')) {
            e.show();
            f.hide()
        }
    }
    conditions.on('change', function() {
        if ($(this).val() != 'ja') {
            button.prop('disabled', true);
            f.hide();
            e.show();
        } else {
            button.prop('disabled', false);
            e.hide();
            f.show();
        }
    })
})
