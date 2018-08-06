if __name__ == '__main__':
    from termcolor import cprint
    import sys
    if len(sys.argv) != 2:
        print('\n')
        cprint('> Usage: python3 run.py [PORT]', 'cyan')
        print('\n')
        exit()
    port = int(sys.argv[1])    
    cprint('     .___             .__       .__    .__             .__         ', 'cyan')
    cprint('   __| _/___________  |__| ____ |  |__ |__| ____  ____ |__| ____   ', 'cyan')
    cprint('  / __ |\_  __ \__  \ |  |/ ___\|  |  \|  |/ ___\/  _ \|  |/    \  ', 'cyan')
    cprint(' / /_/ | |  | \// __ \|  \  \___|   Y  \  \  \__(  <_> )  |   |  \ ', 'cyan')
    cprint(' \____ | |__|  (____  /__|\___  >___|  /__|\___  >____/|__|___|  / ', 'cyan')
    cprint('      \/            \/        \/     \/        \/              \/  ', 'cyan')
    cprint('                             {}'.format(port), 'magenta')
    from src.routes import app
    app.run(host='127.0.0.1', port=port)
