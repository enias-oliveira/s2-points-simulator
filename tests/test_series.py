import times.serie_a as sa
import times.serie_b as sb


def test_serie_a_dicts():

    expected = {
        "time": "Athletico-PR",
        "total_de_pontos": 0,
        "partidas_jogadas": 0,
        "saldo_gols": 0,
        "gols_pro": 0,
    }

    result = sa.serie_a[0]

    assert result == expected


def test_serie_b_dicts():

    expected = {
        "time": "América Mineiro",
        "total_de_pontos": 0,
        "partidas_jogadas": 0,
        "saldo_gols": 0,
        "gols_pro": 0,
    }

    result = sb.serie_b[0]

    assert result == expected
