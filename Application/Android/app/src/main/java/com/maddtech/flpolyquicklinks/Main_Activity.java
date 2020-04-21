package com.maddtech.flpolyquicklinks;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.widget.ImageButton;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.view.menu.MenuBuilder;
import androidx.appcompat.widget.Toolbar;

public class Main_Activity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main_activity);
        Toolbar myToolbar = (Toolbar) findViewById(R.id.my_toolbar);
        setSupportActionBar(myToolbar);
        getSupportActionBar().setTitle(null);
        myToolbar.setOverflowIcon(getResources().getDrawable(R.drawable.ic_icon));
        TextView title = (TextView) myToolbar.findViewById(R.id.web_url);
        ImageButton Canvas = (ImageButton) findViewById(R.id.canvasB);
        ImageButton Cams = (ImageButton) findViewById(R.id.camsB);
        ImageButton Directory = (ImageButton) findViewById(R.id.directoryB);
        ImageButton Course = (ImageButton) findViewById(R.id.courseB);
        ImageButton Mail = (ImageButton) findViewById(R.id.mailB);

    }
    public void goToCanvas (View view) {
        goToUrl ( "https://floridapolytechnic.instructure.com/login");
    }
    public void goToCams (View view) {
        goToUrl ( "https://cams.floridapoly.org/student/login.asp");
    }
    public void goToDirectory (View view) {
        goToUrl ( "https://floridapoly.edu/faculty-staff-directory/");
    }
    public void goToCourseCat (View view) {
        goToUrl ( "http://catalog.floridapoly.edu/");
    }
    public void goToMail (View view) {
        goToUrl ( "https://outlook.office.com/owa/?realm=flpoly.org");
    }

    private void goToUrl (String url) {
        Intent intent = new Intent(this, Webview_Activity.class);
        intent.putExtra("url", url);
        startActivity(intent);
    }

    @SuppressLint("RestrictedApi")
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        MenuInflater inflater = getMenuInflater();
        inflater.inflate(R.menu.popup_menu, menu);
        if(menu instanceof MenuBuilder){
            MenuBuilder m = (MenuBuilder) menu;
            //noinspection RestrictedApi
            m.setOptionalIconsVisible(true);
        }

        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {


        switch (item.getItemId()) {
            case R.id.profile:
                Intent Home=new Intent(Main_Activity.this,Profile_Activity.class);
                startActivity(Home);
                break;
        }
        return true;
    }



}
