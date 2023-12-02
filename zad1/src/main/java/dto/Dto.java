package dto;

import domain.Movie;

import java.util.List;

public class Dto {
    private List<Movie> movieList;

    public Dto(List<Movie> movieList) {
        this.movieList = movieList;
    }

    public List<Movie> getMovieList() {
        return movieList;
    }

    public void addMovie(Movie movie) {
        if (movie == null) {
            throw new NullPointerException();
        } else {
            this.movieList.add(movie);
        }
    }

    public boolean removeMovie(Movie movie) {
        if (this.findMovie(movie)) {
            this.movieList.remove(movie);
            return true;
        }
        return false;
    }

    public boolean findMovie(Movie movie) {
        return this.movieList.contains(movie);
    }

    public Movie getMovie(Movie movie) {
        if (this.findMovie(movie)) {
            int index = this.movieList.indexOf(movie);
            return this.movieList.get(index);
        }
        return null;
    }
}
