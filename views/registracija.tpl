% rebase('osnova.tpl', menu = False)
<form method="POST">
    <div class="field">
        <label class="label">Ime restavracije</label>
        <div class="control">
            <input class="input" name="ime_restavracije" type="text" placeholder="ime restavracije" required>
        </div>
        % if napaka:
        <p class="help is-danger">{{ napaka }}</p>
        % end
    </div>
    <div class="field">
        <label class="label">Geslo</label>
        <div class="control">
            <input class="input" name="geslo" type="password" placeholder="geslo" required>
        </div>
    </div>
    <div class="field is-grouped">
        <div class="control">
            <button class="button is-info">Registriraj se</button>
        </div>
    </div>
</form>