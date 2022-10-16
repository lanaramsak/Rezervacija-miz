% rebase('osnova.tpl', menu = True)

<div class="notification is-danger is-one-half">
    POZOR! Če izbrišete lokacijo, boste z njo izbrisali tudi vse mize pod to lokacijo, želite s tem nadaljevati?
    <br><br>
    <div class="level">
        <div class="level-left">
            <div class="level-item">
                <form method="POST">
                <div class="control">
                    <button class="button">Izbriši</button>
                </div>
                </form>
            </div>
            <div class="level-item">
                <a href="/pregled_miz/"><button class="button">Prekliči</button></a>
            </div>
        </div>
    </div>
</div>