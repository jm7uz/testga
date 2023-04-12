<?php

ob_start();
error_reporting(0);
header('Content-Type: application/json');

function info($id){
    $codertj = curl_init();   
    curl_setopt($codertj, CURLOPT_URL, "https://save-from.net/api/convert");
    curl_setopt($codertj, CURLOPT_HTTPHEADER, array(
    'Origin: https://save-from.net', 
    'Referer: https://save-from.net/', 
    'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'));
    curl_setopt($codertj, CURLOPT_POST, true);
    curl_setopt($codertj, CURLOPT_POSTFIELDS, "url=".$id);
    curl_setopt($codertj, CURLOPT_RETURNTRANSFER, true);
    $response = curl_exec($codertj);
    curl_close($codertj);

    return $response;
}

$res = info($_GET["url"]);
$arr = json_decode($res,1);

echo json_encode($arr, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES);
