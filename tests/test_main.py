from main import jogar_partida, montar_classificacao, main


def test_jogar_partida():

    divisao_test = [
        {
            "time": "Palmeiras",
            "total_de_pontos": 0,
            "partidas_jogadas": 0,
            "saldo_gols": 0,
            "gols_pro": 0,
        },
        {
            "time": "Flamengo",
            "total_de_pontos": 0,
            "partidas_jogadas": 0,
            "saldo_gols": 0,
            "gols_pro": 0,
        },
    ]

    time_a = {
        "time": "Palmeiras",
        "total_de_pontos": 0,
        "partidas_jogadas": 0,
        "saldo_gols": 0,
        "gols_pro": 0,
    }

    time_b = {
        "time": "Flamengo",
        "total_de_pontos": 0,
        "partidas_jogadas": 0,
        "saldo_gols": 0,
        "gols_pro": 0,
    }

    result = jogar_partida(divisao_test, time_a, time_b)

    assert result == divisao_test
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["time"] == divisao_test[0]["time"]


def test_montar_classificacao():

    expected = [
        {
            "time": "Palmeiras",
            "total_de_pontos": 6,
            "partidas_jogadas": 2,
            "saldo_gols": 10,
            "gols_pro": 10,
        },
        {
            "time": "Fortaleza",
            "total_de_pontos": 3,
            "partidas_jogadas": 2,
            "saldo_gols": 6,
            "gols_pro": 8,
        },
        {
            "time": "Bahia",
            "total_de_pontos": 3,
            "partidas_jogadas": 2,
            "saldo_gols": 5,
            "gols_pro": 7,
        },
        {
            "time": "Santos",
            "total_de_pontos": 3,
            "partidas_jogadas": 2,
            "saldo_gols": 5,
            "gols_pro": 6,
        },
        {
            "time": "Coritiba",
            "total_de_pontos": 1,
            "partidas_jogadas": 2,
            "saldo_gols": 4,
            "gols_pro": 4,
        },
    ]

    test_division = [
        {
            "time": "Bahia",
            "total_de_pontos": 3,
            "partidas_jogadas": 2,
            "saldo_gols": 5,
            "gols_pro": 7,
        },
        {
            "time": "Coritiba",
            "total_de_pontos": 1,
            "partidas_jogadas": 2,
            "saldo_gols": 4,
            "gols_pro": 4,
        },
        {
            "time": "Santos",
            "total_de_pontos": 3,
            "partidas_jogadas": 2,
            "saldo_gols": 5,
            "gols_pro": 6,
        },
        {
            "time": "Fortaleza",
            "total_de_pontos": 3,
            "partidas_jogadas": 2,
            "saldo_gols": 6,
            "gols_pro": 8,
        },
        {
            "time": "Palmeiras",
            "total_de_pontos": 6,
            "partidas_jogadas": 2,
            "saldo_gols": 10,
            "gols_pro": 10,
        },
    ]

    result = montar_classificacao(test_division)

    assert result == expected


def test_main():

    ...
