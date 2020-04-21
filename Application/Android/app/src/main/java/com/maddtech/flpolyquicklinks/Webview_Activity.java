package com.maddtech.flpolyquicklinks;

import android.annotation.SuppressLint;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Bitmap;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.view.View;
import android.view.Window;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;

import java.util.List;

public class Webview_Activity extends AppCompatActivity {

    WebView webView;

    TextView webURL;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.browser_activity);
        Toolbar webToolbar = (Toolbar) findViewById(R.id.web_toolbar);
        setSupportActionBar(webToolbar);
        getSupportActionBar().setTitle(null);
        getSupportActionBar().setDisplayHomeAsUpEnabled(true);
        getSupportActionBar().setDisplayShowHomeEnabled(true);

        webURL = findViewById(R.id.web_url) ;
        String url = getIntent().getStringExtra("url");
        webView = (WebView) findViewById(R.id.webView1);
        WebSettings websetting = webView.getSettings();
        websetting.setJavaScriptEnabled(true);
        websetting.setSupportMultipleWindows(true);
        webView.setWebViewClient(new webViewClient());
        webView.loadUrl(url);

        webToolbar.setNavigationOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(getApplicationContext(),Main_Activity.class));
            }
        });
    }

    private class webViewClient extends WebViewClient {
        @Override
        public void onPageStarted(WebView view, String url, Bitmap favicon) {
            super.onPageStarted(view, url, favicon);
        }

        @Override
        public boolean shouldOverrideUrlLoading(WebView view, String url) {
            view.loadUrl(url);
            return true;
        }

        @Override
        public void onPageFinished(WebView view, String url) {
            final SharedPreferences mSharedPreference= PreferenceManager.getDefaultSharedPreferences(getBaseContext());
            String user1=(mSharedPreference.getString("username", "Default_Value"));
            String pass1=(mSharedPreference.getString("password", "Default_Value"));

            super.onPageFinished(view, url);

            // Update EditText and Action bar
            webURL.setText(view.getUrl().toString());
            String user = user1;
            String pwd = pass1;
            if (url.equals("https://cams.floridapoly.org/student/login.asp")){
                String remove = "@floridapoly.edu";
                String user2 = user1.replaceAll(remove, "");
                view.loadUrl("javascript:(function() { document.getElementById('txtUsername').value = '" + user2 + "';document.getElementById('txtPassword').value='" + pwd + "'; ;})()");
                view.loadUrl("javascript:(function() { var z = document.getElementById('btnLogin').click(); })()");
            }
            else {
                view.loadUrl("javascript:(function() { document.getElementById('userNameInput').value = '" + user + "';document.getElementById('passwordInput').value='" + pwd + "'; ;})()");
                System.out.println("AUTOFILL");
                view.loadUrl("javascript:(function() { var z = document.getElementById('submitButton').click(); })()");
            }

        }
    }
    @Override
    protected void onSaveInstanceState(Bundle outState ){
        super.onSaveInstanceState(outState);
        webView.saveState(outState);
    }

    @Override
    protected void onRestoreInstanceState(Bundle savedInstanceState){
        super.onRestoreInstanceState(savedInstanceState);
        webView.restoreState(savedInstanceState);
    }
}
