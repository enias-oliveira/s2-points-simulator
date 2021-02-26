def create_series_dicts(teams: list):
    def create_dict(team_name):
        return {
            "time": team_name,
            "total_de_pontos": 0,
            "partidas_jogadas": 0,
            "saldo_gols": 0,
            "gols_pro": 0,
        }

    return [create_dict(team) for team in teams]
