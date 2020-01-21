using UnityEngine;
using UnityEngine.Networking;
using System;
using System.Collections;

/*
 * Communicates with the Raspberry Pi by sending input values for vertical and horizontal axes.
 * Author: Jacob Sommer
 * Date: 2020-01-20
 */
public class Car : MonoBehaviour
{

    string IP = "192.168.1.2"; // IP of the Pi
    string port = "5000"; // port that Flask is listening on
    private float prevVert = 0f;
    private float prevHoriz = 0f;

    // Update is called once per frame
    void Update()
    {
        float currentVert = Input.GetAxis("Vertical"); // get input on vertical axis (movement forward and backward; defined in Unity)
        if (currentVert != prevVert) // if change in vertical input found
        {
            prevVert = currentVert; // set previous input to current
            StartCoroutine(move("drive", currentVert)); // send a POST request to the Pi with the new value
        }
        float currentHoriz = Input.GetAxis("Horizontal"); // get input on horizontal axis (steering; defined in Unity)
        if (currentHoriz != prevHoriz)  // if change in horizontal input found
        {
            prevHoriz = currentHoriz; // set previous input to current
            StartCoroutine(move("turn", currentHoriz)); // send a POST request to the Pi with the new value
        }
    }

    /*
     * Sends a POST request to the Pi with the specified values
     * type - Either "drive" or "turn"
     * value - a float between 0 and 1
     */
    IEnumerator move(string type, float value)
    {
        WWWForm form = new WWWForm(); // build form for passing values
        form.AddField("value", value + ""); // pass the value
        UnityWebRequest www = UnityWebRequest.Post("http://" + IP + ":" + port + "/" + type, form); // build POST request
        yield return www.SendWebRequest(); // wait for the request to send

        if (www.isNetworkError || www.isHttpError) // if an error occurs
        {
            Debug.Log(www.error); // log it
        }
    }

}
