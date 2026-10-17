# matplotlib 
GRID_PARAMS = {'lw': .5, 'color': 'grey', 'alpha': .5}
LEGEND_PARAMS = {'fontsize': 12, 'edgecolor': 'black'}
LABEL_PARAMS = {'fontsize': 12, 'labelpad': 12}
TITLE_PARAMS = {'fontsize': 17, 'pad': 10}

# 02_02
groups_palette = ["#00C93C", "#C70000", "#475A7E"]  # палитра для групп из блока 02_02 

# 02_03
col_names_thresholds = [  # имена колонок и пороги для блока 02_03 
    ('sleep_hours', 7),
    ('study_hours_per_day', 5),
    ('mental_health_rating', 7),
    ('attendance_percentage', 90),
]
group_colors = ['#1f77b4', '#d62728', '#2ca02c', "#ff5100"]  # палитра для групп из блока 02_03

# 02_05 - лейблы групп для легенды (блок 02_05) 
YOUNG_LABEL = 'Младшие (17–20 лет)'
ADULT_LABEL = 'Старшие (21–24 года)'

# 02_06 - словари порогов привычек 
THRESHOLDS_BAD = {
    'study': 2,
    'social': 5,
    'netflix': 5,
    'sleep': 5
}
THRESHOLDS_GOOD = {
    'study': 4,
    'social': 1.5,
    'netflix': 2,
    'sleep': 7
}