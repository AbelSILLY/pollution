import plotly.express as px
from plotly.offline import plot

def plotpoll(df):
    """
    Cette fonction affiche la concentration d'un polluant en fonction du temps

    Args:
    df (pd.DataFrame): le data frame des données à afficher
    """
    fig = px.scatter(
        df,
        #x = "date_debut",
        y = "valeur",
        animation_frame = 'date_debut',
        animation_group = 'nom_poll',
        range_x=[-10, 200],
        range_y=[0, 40],
        size='valeur'
    )
    fig.show("notebook")