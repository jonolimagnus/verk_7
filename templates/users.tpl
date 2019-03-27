<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>skráðir notendur</title>
    <link rel="stylesheet" type="text/css" media="screen" href="main.css" />
</head>
<body>
    <p>velkominn á síððna {{ userID }}</p>
    <table border = 1>
        {% for user in userDetails %}
        <tr>
            <td> {{user[0]}}</td>
            <td> {{user[1]}}</td>
            <td> {{user[2]}}</td>
        </tr>
        {% endfor %}
    </table>
    <a href="/" class="button">útskraning</a>
</body>
</html>