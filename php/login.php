<?php
// ======= ⚙️ テストモードの切り替え =======
$useDatabase = false; // true = データベースモード, false = テストモード（固定ユーザー）

if ($useDatabase) {
    // ======= 📦 データベースモード =======
    $host = 'localhost';
    $db   = 'your_database_name';     // データベース名
    $user = 'your_db_user';           // ユーザー名
    $pass = 'your_db_password';       // パスワード
    $charset = 'utf8mb4';

    $dsn = "mysql:host=$host;dbname=$db;charset=$charset";
    $options = [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION];

    // データベース接続
    try {
        $pdo = new PDO($dsn, $user, $pass, $options);
    } catch (PDOException $e) {
        die("データベースへの接続に失敗しました: " . $e->getMessage());
    }

    // フォームから送信されたユーザー名とパスワードを取得
    $username = $_POST['username'];
    $password = $_POST['password'];

    // ユーザー情報を検索
    $stmt = $pdo->prepare("SELECT * FROM account WHERE username = :username AND password = :password");
    $stmt->execute(['username' => $username, 'password' => $password]);
    $user = $stmt->fetch();

    // 結果に応じてリダイレクト
    if ($user) {
        if ($user['authority'] === 'admin') {
            header("Location: ../admin_home.html"); // 管理者ページへ
            exit();
        } elseif ($user['authority'] === 'user') {
            header("Location: ../user_home.html");  // ユーザーページへ
            exit();
        } else {
            echo "権限が不明です。";
        }
    } else {
        echo "ユーザー名またはパスワードが正しくありません。";
    }

} else {
    // ======= 🧪 テスト用（書き込み固定）モード =======
    $username = $_POST['username'];
    $password = $_POST['password'];

    // 固定ユーザー情報で判定（実際のサービスでは使わないでください）
    if ($username === 'admin' && $password === 'admin123') {
        header("Location: ../admin_home.html"); // 管理者ページへ
        exit();
    } elseif ($username === 'user' && $password === 'user123') {
        header("Location: ../user_home.html");  // ユーザーページへ
        exit();
    } else {
        echo "ユーザー名またはパスワードが正しくありません。";
    }
}
?>
