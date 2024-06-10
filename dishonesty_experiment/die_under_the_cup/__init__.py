from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer, Page, WaitPage, Currency as c
)
import random

class Constants(BaseConstants):
    name_in_url = 'die_under_the_cup'
    players_per_group = None
    num_rounds = 4  # Adjust this based on your experimental design
    endowment_loss_frame = c(6)  # Endowment for loss frame

class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
            player.actual_number = random.randint(1, 6)
            if self.round_number == 1:
                player.frame = random.choice(['Gain', 'Loss'])
            else:
                player.frame = player.in_round(1).frame

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    round_number = models.IntegerField()
    frame = models.StringField()
    reported_number = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6],
        widget=widgets.RadioSelect
    )
    actual_number = models.IntegerField()
    selected_for_payoff = models.BooleanField(initial=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.actual_number = random.randint(1, 6)
        if not self.frame:
            self.frame = random.choice(['Gain', 'Loss'])

    def set_payoff(player):
        if player.frame == 'Gain':
            player.payoff = c(player.reported_number if player.reported_number != 6 else 0)
        elif player.frame == 'Loss':
            player.payoff = c(Constants.endowment_loss_frame - (player.reported_number if player.reported_number != 6 else 0))

class Introduction(Page):
    def is_displayed(player):
        return player.round_number == 1

    def before_next_page(self, timeout_happened):
        subsession = self.subsession
        for player in subsession.get_players():
            player.actual_number = random.randint(1, 6)
            player.actual_number = player.actual_number
            break

class RollDice(Page):
    form_model = 'player'
    form_fields = ['reported_number']

    @staticmethod
    def vars_for_template(player):
        return {
            'actual_number': player.actual_number,
            'round_number': player.round_number,
            'total_rounds': Constants.num_rounds
        }

    def before_next_page(player, timeout_happened):
        player.set_payoff()

    def is_displayed(player):
        return player.round_number <= Constants.num_rounds  # Display the page for the specified number of rounds

class Results(Page):
    def is_displayed(player):
        return player.round_number == Constants.num_rounds

    def vars_for_template(player):
        random_round = random.randint(1, Constants.num_rounds)
        for p in player.in_all_rounds():
            p.selected_for_payoff = (p.round_number == random_round)

        selected_round = player.in_round(random_round)
        final_earnings = selected_round.payoff

        return {
            'final_earnings': final_earnings,
            'random_round': random_round,
        }

page_sequence = [Introduction, RollDice, Results]