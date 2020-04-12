if __name__ == '__main__' :
    from domain.control import PathMannanger
    pathMannanger = PathMannanger.PathMannanger(printStatus = True)

    import Chess

    Chess.Chess(pathMannanger).run()
