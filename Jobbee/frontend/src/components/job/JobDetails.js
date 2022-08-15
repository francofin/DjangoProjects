import React, { useEffect } from "react";
import moment from 'moment';
import mapboxgl from 'mapbox-gl';

const JobDetails = ({job, candidates}) => {
    console.log(job)
    console.log(candidates)

    mapboxgl.accessToken = process.env.MAPBOX_ACCESS_TOKEN;
    

    useEffect(() => {
      const loadMap = async() => {
        // const coordinate = job.point;
        // const lat = coordinate.split("(")[1].split(")")[0].split(" ")[0]
        // const long = coordinate.split("(")[1].split(")")[0].split(" ")[1]

        // console.log(lat)
        // console.log(long)
        const coordinate = job.point.split("(")[1].replace(")", "").split(" ");

        const map = new mapboxgl.Map({
          container: 'job-map', // container ID
          style: 'mapbox://styles/mapbox/streets-v11', // style URL
          center: coordinate, // starting position [lng, lat]
          zoom: 9, // starting zoom
          // projection: 'globe' // display the map as a 3D globe
          });

          new mapboxgl.Marker().setLngLat(coordinate).addTo(map)

          return map;
        
      }

      loadMap();
    }, [])
  return (
    <div className="job-details-wrapper">
      <div className="container container-fluid">
        <div className="row">
          <div className="col-xl-9 col-lg-8">
            <div className="job-details p-3">
              <div className="job-header p-4">
                <h2>{job.title}</h2>
                <span>
                  <i aria-hidden className="fas fa-building"></i>
                  <span> {job.industry}</span>
                </span>
                <span className="ml-4">
                  <i aria-hidden className="fas fa-map-marker-alt"></i>
                  <span> {job.address}</span>
                </span>

                <div className="mt-3">
                  <span>
                    <button className="btn btn-primary px-4 py-2 apply-btn">
                      Apply Now
                    </button>
                    <span className="ml-4 text-success">
                      <b>{candidates}</b> candidates has applied to this job.
                    </span>
                  </span>
                </div>
              </div>

              <div className="job-description mt-5">
                <h4>Description</h4>
                <p>
                  {job.section_one}
                </p>

                <p>
                  {job.section_two}
                </p>

                <p>
                  {job.section_three}
                </p>

                <p>
                  {job.section_four}
                </p>

                <p>
                  {job.section_five}
                </p>
              </div>

              <div className="job-summary">
                <h4 className="mt-5 mb-4">Job Summary</h4>
                <table className="table table-striped">
                  <tbody>
                    <tr>
                      <td>Job Type</td>
                      <td>:</td>
                      <td>{job.jobType}</td>
                    </tr>

                    <tr>
                      <td>Job Industry</td>
                      <td>:</td>
                      <td>{job.industry}</td>
                    </tr>

                    <tr>
                      <td>Expected Salary</td>
                      <td>:</td>
                      <td>${job.salary}</td>
                    </tr>

                    <tr>
                      <td>Education</td>
                      <td>:</td>
                      <td>{job.education}</td>
                    </tr>

                    <tr>
                      <td>Experience</td>
                      <td>:</td>
                      <td>{job.experience}</td>
                    </tr>

                    <tr>
                      <td>Company</td>
                      <td>:</td>
                      <td>{job.company}</td>
                    </tr>
                  </tbody>
                </table>
              </div>

              <div className="job-location">
                <h4 className="mt-5 mb-4">Job Location</h4>
                <div id='job-map' style={{height:520, width:'100%'}}>

                </div>
              </div>
            </div>
          </div>

          <div className="col-xl-3 col-lg-4">
            <div className="job-contact-details p-3">
              <h4 className="my-4">More Details</h4>
              <hr />
              <h5>Email Address:</h5>
              <p>{job.email}</p>

              <h5>Job Posted:</h5>
              <p>{moment.utc(job.created_at).local().startOf('second').fromNow()}</p>

              <h5>Last Date:</h5>
              <p>{job.applicationExpiry.substring(0,10)}</p>
            </div>

            <div className="mt-5 p-0">
              <div className="alert alert-danger">
                <h5>Note:</h5>
                You can no longer apply to this job. This job is expired. Last
                date to apply for this job was: <b>15-2-2022</b>
                <br /> Checkout others job on Jobbee.
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default JobDetails;