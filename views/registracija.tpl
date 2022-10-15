% rebase('osnova.tpl', menu = False)
<form method="POST">
    <div class="field">
        <label class="label">Uporabniško ime</label>
        <div class="control has-icons-left">
            <input class="input" name="ime_restavracije" type="text" placeholder="ime restavracije">
            <span class="icon is-small is-left">
                <i class="fas fa-user"></i>
            </span>
        </div>
        % if napaka:
        <p class="help is-danger">{{ napaka }}</p>
        % end
    </div>
    <div class="field">
        <label class="label">Geslo</label>
        <div class="control has-icons-left">
            <input class="input" name="geslo" type="password" placeholder="geslo">
            <span class="icon is-small is-left">
                <i class="fas fa-lock"></i>
            </span>
        </div>
    </div>
    <div class="field is-grouped">
        <div class="control">
            <button class="button is-link">Registriraj se</button>
        </div>
    </div>
</form>