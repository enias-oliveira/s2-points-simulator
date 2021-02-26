from itertools import combinations
from operator import itemgetter
from prettytable import PrettyTable
from random import randint

import times.serie_a as sa
import times.serie_b as sb


def jogar_partida(divisao: list, time_a: dict, time_b: dict) -> list:

    time_a_goals = randint(0, 3)
    time_b_goals = randint(0, 3)

    def atualizar_pontos(team, points):
        team["total_de_pontos"] += points

    def atualizar_gols_pro(team, goals):
        team["gols_pro"] += goals

    def atualizar_saldo_gols(team, saldo):
        team["saldo_gols"] += saldo

    def atualizar_partidas_jogadas(team):
        team["partidas_jogadas"] += 1

    def atualizar_time(time, time_goals, time_adversary_goals):
        saldo_gols = time_goals - time_adversary_goals
        atualizar_saldo_gols(time, saldo_gols)
        atualizar_partidas_jogadas(time)
        atualizar_gols_pro(time, time_goals)

    def atualizar_empate(time, time_goals, time_adversary_goals):
        atualizar_time(time, time_goals, time_adversary_goals)
        PONTOS_POR_EMPATE = 1
        atualizar_pontos(time, PONTOS_POR_EMPATE)

    def atualizar_time_vencendor(time, time_goals, time_adversary_goals):
        atualizar_time(time, time_goals, time_adversary_goals)
        PONTOS_POR_VITORIA = 3
        atualizar_pontos(time, PONTOS_POR_VITORIA)

    if time_a_goals < time_b_goals:
        atualizar_time_vencendor(time_b, time_b_goals, time_a_goals)
        atualizar_time(time_a, time_a_goals, time_b_goals)

    elif time_a_goals > time_b_goals:

        atualizar_time_vencendor(time_a, time_a_goals, time_b_goals)
        atualizar_time(time_b, time_b_goals, time_a_goals)

    else:
        atualizar_empate(time_a, time_a_goals, time_b_goals)
        atualizar_empate(time_b, time_b_goals, time_a_goals)

    def update_division(division, *teams):
        division_teams_names = [team["time"] for team in division]

        for team in teams:
            team_name = team["time"]
            team_index = division_teams_names.index(team_name)

            division[team_index] = team

        return division

    return update_division(divisao, time_a, time_b)


def montar_classificacao(divisao: list):

    sorted_division = sorted(
        divisao,
        key=itemgetter("total_de_pontos", "saldo_gols", "gols_pro"),
        reverse=True,
    )

    return sorted_division


def main(division):

    teams_matchup = list(combinations(range(0, 20), 2))

    def play_games(division, matchups):
        for match in matchups:

            team_a = division[match[0]]
            team_b = division[match[1]]

            jogar_partida(division, team_a, team_b)

    play_games(division, teams_matchup)

    ranked_division = montar_classificacao(division)

    table_headers = [
        "Posição",
        "Time",
        "Partidas jogadas",
        "Pontuação",
        "Saldo de Gols",
        "Gols Pro",
    ]

    division_table = PrettyTable()

    division_table.field_names = table_headers

    for rank, team in enumerate(ranked_division, start=1):
        sorted_team = sorted(team.items())
        goals_pro, played_games, goals_saldo, team, points = [
            value[1] for value in sorted_team
        ]
        division_table.add_row(
            [rank, team, played_games, points, goals_saldo, goals_pro]
        )

    print(division_table)


if __name__ == "__main__":

    serie_a_teams = sa.serie_a
    serie_b_teams = sb.serie_b

    main(serie_a_teams)
    print("\n ------------------------------------------------- \n")
    main(serie_b_teams)
